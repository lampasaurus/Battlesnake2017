import bottle
import os

snek_ID = "6723ed50-e6d8-478c-a5a0-e0cedad671d4"

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = 'https://static.wixstatic.com/media/e7c4de_1766eade149b4336a06701c896bb6246.png/v1/fill/w_24,h_24,al_c,lg_1/e7c4de_1766eade149b4336a06701c896bb6246.png' 

    return {
        'color': '#45FD3D',
        'head': head_url
    }
def abs( value):
    if value > 0 :
        return value
    if value < 0 :
        return -1*value


def best_food(head, data):
    smallest_D = 1000000000
    for food in data['food']:
        x_delta = abs( head[0] - food[0] )
        y_delta = abs( head[1] - food[1] )
        distance = x_delta + y_delta
        if distance < smallest_D
            smallest_D = distance
            best_coord = food
    return best_coord

def coord_check(data, coord)
    for snake in data['snakes']
        for coordinates in snake['coords']
            if(coord == coordinates)
                return True
    return False


@bottle.post('/start')
def start():
    data = bottle.request.json
    return {
        'taunt': 'cluster ftw'
    }
    
    
def check_walls(head, movement_priority, data):

    if (head[0]+1 == data["width"]):
        movement_priority[3] = -1000
    #there is a wall to the right
    if (head[0] == 0):
        movement_priority[2] = -1000
    #there is a wall to the left
    if (head[1] == 0):
    movement_priority[0] = -1000
    #there is a wall to the above
    if (head[1] == datat["height"]):
        movement_priority[1] = -1000
    #there is a wall below

    return movement_priority
	
	
def snekdar(head, movement_priority, data):
    if(check_coord(data,[head[0], head[1]-1]))
        movement_priority[0]= -1000
    if(check_coord(data,[head[0], head[1]+1]))
        movement_priority[1]= -1000
    if(check_coord(data,[head[0]-1, head[1]]))
        movement_priority[2]= -1000
    if(check_coord(data,[head[0]+1, head[1]]))
        movement_priority[3]= -1000
    #cardinal directions above
    #corner checks --> we can try to make a size check too
    if(check_coord(data, [head[0] -1, head[1] -1] ))
        movement_priority[1]++
        movement_priority[3]++
    if(check_coord((data, [head[0] -1, head[1] +1] )))
        movement_priority[0]++
        movement_priority[3]++
    if(check_coord((data, [head[0] +1, head[1] +1] )))
        movement_priority[0]++
        movement_priority[2]++
    if(check_coord((data, [head[0] +1, head[1] -1] )))
        movement_priority[1]++
        movement_priority[2]++
	return movement_priority
	
	
def check_food(head, movement_priority, data):
    
	return movement_priority
    

@bottle.post('/move')

def move():
    data = bottle.request.json
    #finds our snake based on ID
    my_snake = None
    for snake in data['snakes']:
        if snake['id'] == snek_ID:
            my_snake = snake
    
    #my_snake['coords'][0] = head of snake
    
    movement_priority = { 0,  0, 0, 0}
    #call functions to figure out snake behaviour here
    #check for walls
    movement_priority = check_walls(my_snake['coords'][0], movement_priority, data)
    #check for snakes
    movement_priority = snekdar(my_snake['coords'][0], movement_priority, data)
    #check for food 
    movement_priority = check_food(my_snake['coords'][0], movement_priority, data)
    
  	count = 0
  	best_option= -1
    while(count<4):
    	if(movement_priority[count]>best_option):
    		best_option = count
    	
    
	if(best_option == 0):
        return {'move':'up',
                'taunt':'upwards' }
    if(best_option == 1):
        return {'move':'down',
                'taunt':'downwards' }
    if(best_option == 2):
        return {'move':'left',
                'taunt':'west movement' }
    if(best_option == 3):
        return {'move':'right',
                'taunt':'east movement' }
    



@bottle.post('/end')
def end():
    data = bottle.request.json
    return {
        'taunt': 'Yippie-ki-yay, motherfucker!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
