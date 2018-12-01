from game import Game
from agent import DQN

game=Game()
agent = DQN(11, 4, 1000000, 0.01, 500)
global_step=0
episode=0

k = input("load_saved?")
if k == "yes":
    agent.load_model()
    print("loaded")
input("press enter to go")
while True:
    episode+=1
    done = False
    state = game.reset()
    run =0 
    while True:
        run +=1
        action = agent.get_action(state)
        new_state, reward, done = game.Step(action)
        agent.save_data(state,action,reward,new_state,done)
        state=new_state
        
        if len(agent.memory) >= agent.run_start:
            agent.train_model()
        
        global_step+=1
        if done:
            agent.update_target_model()
            print("Ep|%d"%episode,"|global step:%d"%global_step,"|action len:%d"%run,"|epsilon:%f"%agent.epsilon,"|score:%d"%game.score)
            break
    
    if episode%10 == 0:
        agent.save_model()
        
    if agent.epsilon > 0.05:
        agent.epsilon *= 0.9
    
