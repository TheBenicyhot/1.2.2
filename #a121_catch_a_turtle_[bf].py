#a121_catch_a_turtle_[bf].py
# a121_catch_a_turtle.py
#-----import statements-----(20min)
import turtle as trtl
import random as rand 
import leaderboard as lb
#-----game configuration----(3hr)
spot_color="pink"
spot_shape="circle"
spot_size=2
score=0  


font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

def update_score():
 global score # gives this function access to the score that was created above
 score_writer.clear()
 score += 1
 score_writer.write(score, font=font_setup)
 

font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----(1hr)
spot=trtl.Turtle()
score_writer=trtl.Turtle()
spot.penup()
score_writer.penup()
spot.shape(spot_shape)
spot.color(spot_color)
spot.shapesize(spot_size)
counter =  trtl.Turtle()
counter.penup()
counter.goto(-200,-200)
#-----game functions--------(1hr)


def spot_clicked(x,y):
 if (timer_up == False):
   update_score()
   change_position()
 else:
   counter.hideturtle()
   

def change_position():
 new_xpos=rand.randint(1,400)
 new_ypos=rand.randint(1,300)
 spot.goto(new_xpos,new_ypos)
 
 score_writer.goto(300,200)



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
#-----events----------------(4hr)

spot.onclick(spot_clicked)


wn = trtl.Screen()

wn.ontimer(countdown, counter_interval) 

wn.mainloop()