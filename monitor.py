import csv
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

'''
Plotting inspired by 
https://github.com/baek-jinoo/RL-Quadcopter-2/blob/master/runner.py
'''
class Monitor():
    def __init__(self,
                 labels,
                 labels_per_episode,
                 results_file='results.csv',
                 episodic_file='episodic_results.csv'):
        self.labels = labels
        self.labels_per_episode = labels_per_episode
        self.results_file = results_file
        self.episodic_file = episodic_file

        # Initialize plots
        plt.close('all')        
        fig1, (reward, avg_reward, position, rotors1_3, rotors2_4, speed, angular) = plt.subplots(7, 1)
        reward.set_title("Rewards")
        avg_reward.set_title("Average rewards")
        position.set_title("Position")
        rotors1_3.set_title("Rotors 1 & 3")
        rotors2_4.set_title("Rotors 2 & 4")
        speed.set_title("Velocity per")
        angular.set_title("angular speeds")
        fig1.set_size_inches(4, 9)
        plt.tight_layout(pad=0.4, w_pad=1., h_pad=1.0)
                
        plt.tight_layout(w_pad=1., h_pad=1.0)
        self.fig1 = fig1
        self.rotors1_3 = rotors1_3
        self.rotors2_4 = rotors2_4
        self.position = position
        self.reward = reward
        self.avg_reward = avg_reward
        self.speed = speed
        self.angular = angular
    
    def write(self, all_step_results, all_episode_step_result):
        with open(self.results_file, 'w') as csvfile, open(self.episodic_file, 'w') as episodic_csvfile:
            writer = csv.writer(csvfile)
            episode_writer = csv.writer(episodic_csvfile)
            writer.writerow(self.labels)
            episode_writer.writerow(self.labels_per_episode)
            for step_results in all_step_results:
                writer.writerow(step_results)
            for episode_step_result in all_episode_step_result:
                episode_writer.writerow(episode_step_result)



    def plot(self, results, episode_results, per_episode):
        self.plot_reward(results)
        self.plot_average_reward(episode_results)
        self.plot_position(per_episode)
        self.plot_rotors_1_3(per_episode)
        self.plot_rotors_2_4(per_episode)
        self.plot_speed(per_episode)
        self.plot_angular(per_episode)

    def plot_reward(self, results):
        self.reward.plot(results['reward'])
        self.fig1.canvas.draw()

    def plot_average_reward(self, episode_results):
        self.avg_reward.plot(episode_results['mean_reward'])
        self.fig1.canvas.draw()

    def plot_position(self, per_episode):
        self.position.clear()
        self.position.plot(per_episode['time'], per_episode['x'], label='x', color='green')
        self.position.plot(per_episode['time'], per_episode['y'], label='y', color='red')
        self.position.plot(per_episode['time'], per_episode['z'], label='z', color='blue')
        self.position.legend(loc="upper right")
        self.position.set_title("Position")
        self.fig1.canvas.draw()

    def plot_rotors_1_3(self, per_episode):
        self.rotors1_3.clear()
        self.rotors1_3.plot(per_episode['time'], per_episode['rotor_speed1'], label='1', color='green')
        self.rotors1_3.plot(per_episode['time'], per_episode['rotor_speed3'], label='3', color='blue')
        self.rotors1_3.set_title("Rotors 1 & 3")
        self.rotors1_3.legend(loc="upper right")
        self.fig1.canvas.draw()
    
    def plot_rotors_2_4(self, per_episode):
        self.rotors2_4.clear()
        self.rotors2_4.plot(per_episode['time'], per_episode['rotor_speed2'], label='2', color='red')
        self.rotors2_4.plot(per_episode['time'], per_episode['rotor_speed4'], label='4', color='magenta')
        self.rotors2_4.set_title("Rotors 2 & 4")
        self.rotors2_4.legend(loc="upper right")
        self.fig1.canvas.draw()
    
    def plot_speed(self, per_episode):
        self.speed.clear()
        self.speed.plot(per_episode['time'], per_episode['x_velocity'], label='x', color='green')
        self.speed.plot(per_episode['time'], per_episode['y_velocity'], label='y', color='red')
        self.speed.plot(per_episode['time'], per_episode['z_velocity'], label='z', color='blue')
        self.speed.legend(loc="upper right")
        self.speed.set_title("Velocity per")
        self.fig1.canvas.draw()

    def plot_angular(self, per_episode):
        self.angular.clear()
        self.angular.plot(per_episode['time'], per_episode['phi'], label='phi', color='green')
        self.angular.plot(per_episode['time'], per_episode['theta'], label='theta', color='red')
        self.angular.plot(per_episode['time'], per_episode['psi'], label='psi', color='blue')
        self.angular.legend(loc="upper right")
        self.angular.set_title("Angular speed")
        self.fig1.canvas.draw()