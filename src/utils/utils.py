class Util(object):
    # class or functions

    @staticmethod
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml"
        }
        return headers

    def common_headers_put_delete_patch_basic_auth(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvmQxMjM="
        }
        return headers

    def common_headers_put_delete_patch_cookie(token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database_file(self):
        pass
