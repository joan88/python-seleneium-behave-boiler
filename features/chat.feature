@chat
Feature: Chat

	As a chatter, 
	I want my messages correctly sent real-time to the proper chattee

	Scenario: Robert chats Mary
		Given I am "Robert"
		When I send the message "Yellow" to "Mary"
		Then "Mary" should see the message "Yellow"

	Scenario: Mary responds to Robert's message
		Given I am "Mary"
		When I send the message "Jello" to "Robert"
		Then "Robert" should see the message "Jello"

	Scenario: Mary cannot see chat between Robert and Patricia
		Given I am "Robert"
		When I send the message "Yow" to "Patricia"
		Then "Mary" should NOT see the message "Yow"

