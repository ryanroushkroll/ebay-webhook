from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def ebay_account_deletion():
    challenge = request.args.get("challenge_code") or request.args.get("challenge")
    if challenge:
        return jsonify({"challengeResponse": challenge})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
