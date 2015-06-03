import web

class Reset:
	def GET(self):
		session.login = 0
		session.kill()
		render = create_render(session.privilege)
		return render.logout()