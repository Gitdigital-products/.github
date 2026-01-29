# main.py - Your Python Flask application for the API

import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS # For handling Cross-Origin Resource Sharing
import time

app = Flask(__name__)
# Enable CORS for your GitHub Pages frontend domain
# In production, replace '*' with your specific frontend domain:
# CORS(app, resources={r"/items/*": {"origins": "https://gitdigital-products.github.io"}})
CORS(app) # Allow all origins for development simplicity, restrict in production!

# --- Mock Data Generation ---
# In a real app, this would come from a database (e.g., Cloud SQL, Firestore)
# or be dynamically generated based on complex business logic.
def generate_mock_item_data(item_id):
    """Generates mock data for a given item_id."""
    if not (1 <= item_id <= 768):
        return None

    name_options = [
        "Digital Asset Token", "Compliance Record", "Oracle Feed Entry",
        "Governance Proposal", "KYC Attestation", "Transaction Metadata",
        "Protocol Event", "Audit Log ID", "Regulatory Filing Ref"
    ]
    status_options = ["Active", "Pending Review", "Archived", "Compliant", "Non-Compliant"]
    
    # Simulate some items having richer data, some simpler
    if item_id % 7 == 0:
        description = f"Detailed description for item {item_id}. This item represents a critical piece of metadata within the GitDigital ecosystem, requiring meticulous auditing and tracking."
    elif item_id % 3 == 0:
        description = f"Standard compliance data point for {name_options[item_id % len(name_options)]}."
    else:
        description = f"General reference entry {item_id}."

    data = {
        "id": item_id,
        "name": f"{random.choice(name_options)} #{item_id}",
        "description": description,
        "status": random.choice(status_options),
        "created_at": f"2023-01-01T{item_id % 24:02d}:{(item_id * 3) % 60:02d}:00Z",
        "tags": random.sample(["security", "finance", "blockchain", "regulatory", "data-integrity"], k=random.randint(1, 3)),
        "metadata_hash": f"0x{hash(f'gitdigital-{item_id}') % (10**16):016x}" # Simulate a hash
    }

    # Simulate an error for certain items to test frontend error handling
    if item_id % 13 == 0 and item_id > 100:
        raise ValueError(f"Simulated internal error for item {item_id}")

    return data

# --- API Endpoints ---
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Returns details for a specific item ID.
    Simulates a network delay and potential errors.
    """
    # Simulate network latency (0.1 to 0.5 seconds)
    time.sleep(random.uniform(0.1, 0.5))

    try:
        item_data = generate_mock_item_data(item_id)
        if item_data:
            return jsonify(item_data), 200
        else:
            return jsonify({"error": "Item not found or invalid ID"}), 404
    except ValueError as e:
        # Catch simulated internal errors
        return jsonify({"error": str(e), "code": "INTERNAL_ERROR"}), 500
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected server error occurred", "code": "UNKNOWN_ERROR"}), 500

# Optional: Root endpoint for health check
@app.route('/', methods=['GET'])
def health_check():
    return "API is running!", 200

# --- Running the Flask app ---
if __name__ == '__main__':
    # Use Gunicorn for production deployments on Cloud Run
    # Flask's built-in server is for development only.
    # In Cloud Run, Gunicorn is typically configured via a Dockerfile or buildpacks.
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


