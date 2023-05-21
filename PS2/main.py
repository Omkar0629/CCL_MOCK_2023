import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/plain"
        for _ in range(5):
            self.response.out.write("Name: Omkar Pawar \n")
            self.response.out.write("Seat Number: T190058671 \n")
            self.response.out.write("Department: Information Technology \n")
            self.response.out.write("\n")  # Add a new line between each iteration

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)