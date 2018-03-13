import gym

#Loading our environment
env = gym.make('CartPole-v0')

for i_episode in range(20):
	# Loading the first step
	observation = env.reset()
	for t in range(100):
		env.render()
		print(observation)
		action = env.action_space.sample()
		observation, reward, done, info = env.step(action)
		if done:
			print("Episode fnished after {} timesteps".format(t+1))
			break