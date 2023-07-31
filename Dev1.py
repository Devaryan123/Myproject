#my project 
from ursina import *
app=Ursina()
speed=1
Sky()
def update():
    global speed
    ball.x+=time.dt*speed
    ball.y+=time.dt*speed
    if held_keys["a"]:
        box1.y+=time.dt*2
    if held_keys["s"]:
        box2.y+=time.dt*2
    if held_keys["z"]:
        box1.y-=time.dt*2
    if held_keys["x"]:
        box2.y-=time.dt*2
    hit_info=ball.intersects()
    if hit_info.hit:
        speed*=-1

ball_texture=load_texture("img_2.png")
paddle_texture=load_texture("img_5.png")
ball=Entity(model="sphere",
            scale=(1,1,1),
            position=(0,2,0),
            collider="box",
            texture=ball_texture,
            rotation=(2,2,0))
box1=Entity(model="cube",
            scale=(0.5,2,1),
            position=(-4,0,0),
            texture=paddle_texture,
            collider="box")
box2=Entity(model="cube",
             scale=(0.5,2,1),
             position=(4,0,0),
             texture=paddle_texture,
             collider="box")
camera.position=(0,0,-40)
app.run()
