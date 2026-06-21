from flask import Flask, request, jsonify
import os
import json

def load_tokens(region):
    try:
        if region == "IND":
            token_str = os.getenv("TOKEN_IND")
        else:
            token_str = os.getenv("TOKEN_BD")
            
        if token_str:
            return json.loads(token_str)
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
