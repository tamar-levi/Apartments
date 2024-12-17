import this

from flask import Blueprint, request, jsonify, flash
import json
from pythonProject.Project.db import db

UserRout = Blueprint('routesUser', __name__)


@UserRout.route('/', methods=['POST'])
def createUser():
    from pythonProject.Project.Action.UserAct import create_user
    try:
        data = request.get_json()
        new_user=create_user(firstName=data['first_name'],lastName=data['last_name'], mail=data['mail'], phon=data['phon'], password=data['password'])
        if new_user:
            return jsonify({'result': 'User created successfully', 'user': {
                'first_name': new_user.firstName,
                'last_name': new_user.lastName,
                'mail': new_user.mail,
                'phon': new_user.phon
            }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except(json.JSONDecodeError, KeyError) as e2:
        print(f"Error parsing JSON or missing key: {str(e2)}")
        return jsonify({'error': 'uesr not added'}), 404


@UserRout.route('/reset_password', methods=['GET'])
def sentResetPassword():
    mail=request.args['mail']
    print(mail)
    try:
     from pythonProject.Project.Action.UserAct import send_reset_email

     flag=send_reset_email(mail)
     return jsonify({'result': flag
     }), 201
    except Exception as e:
     db.session.rollback()
     return jsonify({'error': str(e)}), 500



  # try:
@UserRout.route('/', methods=['PUT'])
def updateUser():
    try:
        data = request.get_json()

        from pythonProject.Project.Action.UserAct import update_user

        user=update_user(first_name=data['first_name'],last_name=data['last_name'], mail=data['mail'], phon=data['phon'])
        print(user)
        if user:
            return jsonify({'result': 'User updated successfully'}), 201
        else:
            return jsonify({'error': 'user not updated'}), 404
    except Exception as e:
            from pythonProject.Project.app import db
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

@UserRout.route('/', methods=['DELETE'])
def delete_user():
    mail=request.args.get('mail')
    from pythonProject.Project.Action.UserAct import delete_user
    try:
     flag=delete_user(mail)
     print(mail)
     if flag:
            return jsonify({'result': 'success'}),201
     else:
         return jsonify({'result': 'failed'}) ,404
    except Exception as e:
     from pythonProject.Project.app import db

     db.session.rollback()
     return jsonify({'error': str(e)}), 500

#
@UserRout.route('/', methods=['GET'])
def getAllUser():
    try:
       from pythonProject.Project.Action.UserAct import get_all_users

       users = get_all_users()
       if users is None:
         return jsonify({'eror': 'no users found'}), 404

       else:
           users_list = []
           for user in users:
               user_dict = {
                   'firstName': user.firstName,
                   'lastName': user.lastName,
                   'mail': user.mail,
                   'phon': user.phon,
                   # נוסיף כאן את כל השדות הנוספים שבמקרה שלך
               }
               users_list.append(user_dict)

           # ממיר את הרשימה ל־JSON
           json_users = json.dumps(users_list)

           return jsonify({'result': json.dumps(json_users)}),201

    except Exception as e:
      from pythonProject.Project.app import db
      db.session.rollback()
      return jsonify({'error': str(e)}), 500

#
@UserRout.route('/<string:mail>', methods=['GET'])
def getUserByMail(mail):
    try:
      from pythonProject.Project.Action.UserAct import get_user_by_mail

      user = get_user_by_mail(mail)
      if user is None:
         return jsonify({'eror': 'no user found'}), 404
      else:
         return jsonify({'result': 'User find successfully', 'user': {
             'first_name': user.firstName,
              'last_name': user.lastName,
              'mail': user.mail,
          'phon': user.phon
           }}), 201
    except Exception as e:
            from pythonProject.Project.app import db
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
@UserRout.route('/reset_password', methods=['PUT'])
def resetPassword():
    try:
        token=request.args['token']
        data = request.get_json()
        from pythonProject.Project.Action.UserAct import reset_password
        user=reset_password(mail=data['mail'],new_password=data['password'],token=token)
        if user:
            return jsonify({'result': 'User change password successfully',}), 201
        else:
            return jsonify({'error': 'user not updated'}), 404
    except Exception as e:
            from pythonProject.Project.app import db
            db.session.rollback()
            return jsonify({'error': str(e)}), 500


