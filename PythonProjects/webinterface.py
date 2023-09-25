from bottle import route, run

led_pins = [18, 23, 24]
led_states = [0, 0, 0]

		
def html_for_led(led):
	l = str(led)
	result = " <input type='button' onClick='changed(" + l + ")'value='LED " + l + "'/>"
	return result
	

		
@route('/')
@route('/<led>')
def index(led="n"):
	if led != "n":
		led_num = int(led)
		led_states[led_num] = not led_states[led_num]
		
	response = "<script>"
	response += "function changed(led)"
	response += "{"
	response += " window.location.href='/' + led"
	response += "}"
	response += "</script>"
	response += '<h1>GPIO Control</h1>'
	response += '<h2>LEDs</h2>'
	response += html_for_led(0)
	response += html_for_led(1)
	response += html_for_led(2)
	return response
run()
