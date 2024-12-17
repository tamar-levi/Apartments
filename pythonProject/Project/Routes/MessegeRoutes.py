
from flask import Blueprint, request, jsonify
import json
from pythonProject.Project.Action.MessegeAct import MessegeService
from pythonProject.Project.Models.MessegeMod import Messege

MessegeRout = Blueprint('routMessege', __name__)


@MessegeRout.route('/', methods=['POST'])
def AaddMessege():
    try:
        body = request.get_json()
        data = json.loads(body)
        messege = MessegeModel(
            data['sender_mail'], data['messege_body'], data['getter_mail'], data['new_messege'], data['Messegeid']
        )
        if messege:
            user = MessegeService.add_message(messege)
            if user is None:
                return jsonify({'error': 'messege not added'}), 404
            return jsonify({'result': user})
        else:
            return jsonify({'error': 'messege not added'}), 404
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error parsing JSON or missing key: {e}")
        return jsonify({'error': 'messege not added'}), 404

@MessegeRout.route('/<int:Messegeid>', methods=['DELETE'])
def delete_Messege(Messegeid):
    Messege = MessegeService.delete_message(Messegeid)
    if Messege is None:
        return jsonify({'error': 'messege not found'}), 404
    return jsonify({'result': 'success'})

@MessegeRout.route('/sent', methods=['GET'])
def get_sent_messages():
    Messeges = MessegeService.get_sent_messages(self=MessegeService)
    if Messeges is None:
        return jsonify({'eror': 'no Messege found'}), 404
    return jsonify({'result': Messeges})
@MessegeRout.route('/received', methods=['GET'])
def get_received_messages():
    Messeges = MessegeService.get_received_messages(self=MessegeService)
    if Messeges is None:
        return jsonify({'eror': 'no Messege found'}), 404
    return jsonify({'result': Messeges})