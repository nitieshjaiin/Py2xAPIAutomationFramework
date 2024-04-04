# Keep the URLs
# API Constants - class which contains all the end points.

class APIConstants(object):

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

# static method can be called without using object, directly using class name you can call it.

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update, PUT, PATCH, DELETE needs booking ID

    def url_patch_put_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)

