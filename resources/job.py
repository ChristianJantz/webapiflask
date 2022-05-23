from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import Job
from flask_jwt_extended import jwt_required, get_jwt_identity


class JobListResource(Resource):
    """ Resource model for all Jobs that are published """
    def get(self):
        """ Return: all jobs in a dictionary with the list jobs properties """

        data = []

        for job in Job.get_all_published():
            if job.is_published is True:
                data.append(job.data)

        
        return {'data': data}, HTTPStatus.OK

   
    @jwt_required()
    def post(self):
        """ create the job post base on the JSON formate form the front end """
        frontend_data = request.get_json()

        job = Job(
            title= frontend_data['title'],
            description= frontend_data['description'],
            salary= frontend_data['salary'],
            
        )
        user_id = get_jwt_identity()
        job.user_id = user_id

        job.save()

        return job.data, HTTPStatus.CREATED


class JobResource(Resource):
    
    def get(self, jobId):
        """sumary_line"""

        job = Job.get_by_id(Id=jobId)

        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        if job.is_published is False:
            return {"message": "job not published"}, HTTPStatus.FORBIDDEN
        
        return job.data, HTTPStatus.OK

    @jwt_required()
    def patch(self, jobId):
        """sumary_line"""

        data = request.get_json()

        job = Job.get_by_id(Id=jobId)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if job.user_id != current_user:
            return {"message" : "access denied"}, HTTPStatus.FORBIDDEN
        
        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']

        job.save()

        return job.data, HTTPStatus.OK

    @jwt_required()    
    def delete(self, jobId):
        """ delete the data """

        job = Job.get_by_id(Id=jobId)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if job.user_id != current_user:
            return {"message" : "access denied"}, HTTPStatus.FORBIDDEN

        job.delete()

        return {}, HTTPStatus.NO_CONTENT

class JobPublishResource(Resource):
    @jwt_required()
    def put(self, jobId):

        job = Job.get_by_id(Id=jobId)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if job.user_id != current_user:
            return {"message" : "access denied"}, HTTPStatus.FORBIDDEN
        
        job.is_published = True
        job.save()

        return {"message": "job is now published"}, HTTPStatus.OK

    @jwt_required()
    def delete(self, jobId):
        job = Job.get_by_id(Id=jobId)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if job.user_id != current_user:
            return {"message" : "access denied"}, HTTPStatus.FORBIDDEN
        
        job.is_published = False
        job.save()

        return {"message":"jos is now draft"}, HTTPStatus.OK