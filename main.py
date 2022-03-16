from time import sleep
import data
import ActionPatterns

d = data.TwData("ashleylxa")


ap = ActionPatterns.Patterns(data.profiles)
ap.SendTweets()
