# Joke Module

This is a joke module which fetches some jokes from  www.goodbadjokes.com and speaks it out through Stephanie.

### Setting Up

- Download this repository and then copy joke_module.py and paste it to the modules subfolder present in Stephanie Package
- Open modules.json file, and add this at the very end before the last ending bracket :

		["JokeModule@TellJoke", ["tell", "joke"]]

- Somewhat like this (Notice there's no comma in the end if it's the last):
		
		[
			[...]
			[...]
			["SomeOtherModule@DoSomeShit", ['just', 'a', 'sample']],
			["SomeOtherModule@DoSomeShit", ['just', 'a', 'sample']],
			["JokeModule@TellJoke", ["tell", "joke"]]
		]

- And that's it.

### Features

- Tells a random joke.
	- tell
	- joke

### Usage

**You**: Hey Stephanie, tell me a joke.

**Stephanie**: What did one snowman say to the other snowman?It smells like carrots out here!

### Demo

joke_module_standalone is used to test how module works.
