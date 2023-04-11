from flask import Blueprint, jsonify
from connections.cluster_client import CLIENT
from flaskr.utils import response_generator