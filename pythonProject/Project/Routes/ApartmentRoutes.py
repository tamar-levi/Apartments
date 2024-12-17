# from flask import Blueprint, request, jsonify
# import json
# from pythonProject.Project.Action.ApartmentAct import ApartmentService
# from pythonProject.Project.Models.ApartmentMod import ApartmentModel, ApartmentType
#
# ApartmentRout = Blueprint('routesApartment', __name__)
#
# @ApartmentRout.route('/',methods=['POST'])
# def AddApartmentRoute():
#  try:
#     body = request.get_json()
#     data = json.loads(body)
#     apartment_model = ApartmentModel(
#         data['neighborhood'],
#         data['street'],
#         data['num_build'],
#         data['num_apartment'],
#         data['num_rooms'],
#         data['floor'],
#         ApartmentType(data['apartmentType']),  # Convert to ApartmentType enum
#         data['meters'],
#         data['air_directions'],
#         data['porch'],
#         data['elevator'],
#         data['yard'],
#         data['furniture'],
#         data['solar_heaters'],
#         data['sukkah'],
#         data['air_conditioner'],
#         data['enter_date'],
#         data['price'],
#         data['flexible_price'],
#         data['description'],
#         data['start_hour'],
#         data['end_hour'],
#         data['takanon'],
#         data['mail'],
#     )
#     if apartment_model:
#         apartment = ApartmentService.add_apartment(apartment_model)
#         if apartment is None:
#             return jsonify({'error': 'apartment not added'}), 404
#         return jsonify({'result': apartment})
#     else:
#         return jsonify({'error': 'apartment not added'}),404
#  except (json.JSONDecodeError, KeyError) as e:
#     print(f"Error parsing JSON or missing key: {e}")
#     return jsonify({'error': 'apartment not added'}), 404
#
#
# @ApartmentRout.route('/',methods=['PUT'])
# def UpdateApartmentRoute():
#     try:
#         body = request.get_json()
#         data = json.loads(body)
#         apartment_model = ApartmentModel(
#             data['neighborhood'],
#             data['street'],
#             data['num_build'],
#             data['num_apartment'],
#             data['num_rooms'],
#             data['floor'],
#             ApartmentType(data['apartmentType']),  # Convert to ApartmentType enum
#             data['meters'],
#             data['air_directions'],
#             data['porch'],
#             data['elevator'],
#             data['yard'],
#             data['furniture'],
#             data['solar_heaters'],
#             data['sukkah'],
#             data['air_conditioner'],
#             data['enter_date'],
#             data['price'],
#             data['flexible_price'],
#             data['description'],
#             data['start_hour'],
#             data['end_hour'],
#             data['takanon'],
#             data['mail'],
#         )
#         if apartment_model:
#             apartment = ApartmentService.update_apartment(apartment_model)
#             if apartment is None:
#                 return jsonify({'error': 'apartment not updated'}), 404
#             return jsonify({'result': apartment})
#         else:
#             return jsonify({'error': 'apartment not updated'}), 404
#     except (json.JSONDecodeError, KeyError) as e:
#         print(f"Error parsing JSON or missing key: {e}")
#         return jsonify({'error': 'apartment not updated'}), 404
#
#
#
# @ApartmentRout.route('/<int:apartment_id>', methods=['DELETE'])
# def delete_apartment(apartment_id):
#     apartment = ApartmentService.delete_apartment(apartment_id)
#     if apartment is None:
#         return jsonify({'error': 'apartment not found'}), 404
#     return jsonify({'result': 'success'})
#
#
#
# @ApartmentRout.route('/',methods=['GET'])
# def getAllApartment():
#     apartments = ApartmentService.get_all_apartments(self=ApartmentService);
#     if apartments is None:
#         return jsonify({'eror': 'no apartments found'}),404
#     return jsonify({'result': apartments})
#
#
# @ApartmentRout.route('/<string:mail>',methods=['GET'])
# def getApartmentByUser(mail):
#     apartments = ApartmentService.get_apartment_by_user(mail)
#     if apartments is None:
#         return jsonify({'eror': 'no apartments found'}),404
#     return jsonify({'result': apartments})

import this

from flask import Blueprint, request, jsonify, flash
import json
from pythonProject.Project.db import db

ApartmentRoute = Blueprint('routesApartment', __name__)


@ApartmentRoute.route('/', methods=['POST'])
def createApartment():
    from pythonProject.Project.Action.ApartmentAct import create_Apartment
    try:
        data = request.get_json()
        new_apartment=create_Apartment( neighborhood=data['neighborhood'],
            street=data['street'],
            num_build=data['num_build'],
            num_apartment=data['num_apartment'],
            num_rooms=data['num_rooms'],
            floor=data['floor'],
            apartmentType=ApartmentType(data['apartmentType']),  # Convert to ApartmentType enum
            meters=data['meters'],
            air_directions=data['air_directions'],
            porch=data['porch'],
            elevator=data['elevator'],
            yard=data['yard'],
            furniture=data['furniture'],
            solar_heaters=data['solar_heaters'],
            sukkah=data['sukkah'],
            air_conditioner=data['air_conditioner'],
            enter_date=data['enter_date'],
            price=data['price'],
            flexible_price=data['flexible_price'],
            description=data['description'],
            start_hour=data['start_hour'],
            end_hour=data['end_hour'],
            takanon=data['takanon'],
            user_mail=data['user_mail'],)
        if new_apartment:
            return jsonify({'result': 'Apartment created successfully', 'apartment': {
                'neighborhood':new_apartment.neighborhood,
                'street':new_apartment.street,
                'num_apartment':new_apartment.num_apartment,
                'num_rooms':new_apartment.num_rooms,
                'floor':new_apartment.floor,
                'apartmentType':new_apartment.apartmentType,
                 'meters':new_apartment.meters,
                'air_directions': new_apartment.air_directions,
                'porch':new_apartment.porch,
                'elevator':new_apartment.elevator,
                'yard':new_apartment.yard,
                'furniture':new_apartment.furniture,
                'solar_heaters':new_apartment.solar_heaters,
                 'sukkah':new_apartment.sukkah,
                'air_conditioner':new_apartment.air_conditioner,
               'enter_date':new_apartment.enter_date,
               'price':new_apartment.price,
                'flexible_price':new_apartment.flexible_price,
                'description':new_apartment.description,
                'start_hour':new_apartment.start_hour,
               'end_hour':new_apartment.end_hour,
               'takanon':new_apartment.takanon,
               'user_mail':new_apartment.user_mail
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


