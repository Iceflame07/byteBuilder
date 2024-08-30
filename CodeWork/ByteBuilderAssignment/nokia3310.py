menu ="""

1->Phonebook
2->Messages
3->Chat
4->Call register
5->Tones
6->Settings
7->Call divert
8->Games
9->Calculator
10->Reminders
11->Clock
12->Profiles
13->SIM services
""";

option = int(input(menu))

if option == 1:
	print("phonebook")

	phonebook_menu ="""
	1.search
	2.service Nos.
	3.add Name
	4.clear
	5.edit
	6.assign Tone
	7.send b'card
	8.options
	9->speed dials
	10->voice tags
	""";

	phonebook_option = int(input(phonebook_menu))
	if phonebook_option == 1:
		print("search")
	if phonebook_option == 2:
		print("service_nos")
	if phonebook_option == 3:
		print("add_name")
	if phonebook_option == 4:
		print("clear")
	if phonebook_option == 5:
		print("edit")
	if phonebook_option == 6:
		print("assign_tone")
	if phonebook_option == 7:
		print("send_b'card")
	if phonebook_option == 8:
		print("options")
	if phonebook_option == 9:
		print("speed_dials")
	if phonebook_option == 10:
		print("voice_tags")
	if phonebook_option == 0:
		print("back_to_phonebook")
	
	print("Option")

	option_menu =""" 
		1->Type of view
		2->Memory status
		""";

	phonebook_option = int(input(option_menu))
	if phonebook_option == 1:
		print("type_of_view")
	if phonebook_option == 2:
		print("memory_status")
	if phonebook_option == 0:
		print("back_to_phonebook")

elif option == 2:
	print("Messages")

	message_menu ="""
	1->Write messages		
	2->Inbox
	3->Outbox
	4->Picture messages
	5->Templates
	6->Smileys
	7->Message settings
	8->Info service
	9->Voice mailbox number
	10->Service command editor
	""";
	
	messages_option = int(input(messages_menu))
	if messages_option == 1:
		print("write_messages")
	if messages_option == 2:
		print("inbox")
	if messages_option == 3:
		print("outbox")
	if messages_option == 4:
		print("picture_messages")
	if messages_option == 5:
		print("templates")
	if messages_option == 6:
		print("smiley")
	if messages_option == 7:
		print("message_settings")
	if messages_option == 8:
		print("info_service")
	if messages_option == 9:
		print("voice_mailbox_number")
	if messages_option == 10:
		print("service_command_editor")
	if message_option == 0:
		print("back_to_message")

	print("Set_1")

	set_1_menu ="""
		1->Message center service
		2->Message sent as
		3->Message validity
		""";

	set_1_option = int(input(set_1_menu))
	if set_1_option == 1:
			print("message_center_number")
	if set_1_option == 2:
			print("message_sent_as")
	if set_1_option == 3:
			print("message_validity")

	print("Common")

	common_menu ="""
		1->Delivery report
		2->Reply via same centre
		3->Character support
		""";
	
	common_option = int(input(common_menu))
	if set_1_option == 1:
			print("delivery_report")
	if set_1_option == 2:
			print("reply_via_same_center")
	if set_1_option == 3:
			print("character_support")

elif option == 3:
	print("Chat")

	chat_menu ="""
	""";

	chat_option = int(input(chat_menu))
	if chat_option == 1:
		print("chat")

elif option == 4:
	print("Call register")

	call_register_menu ="""
	1->Missed calls		
	2->Received calls
	3->Dialed calls
	4->Erase recent call lists
	5->Show call durations
	6->Show call cost
	7->Call cost settings
	8->Prepaid credit
	""";

	call_register_option = int(input(call_register_menu))
	if call_register_option == 1:
		print("missed_calls")
	if call_register_option == 2:
		print("received_calls")
	if call_register_option == 3:
		print("dialed_numbers")
	if call_register_option == 4:
		print("erase_recent_call_list")
	if call_register_option == 5:
		print("show_call_duration")

	print("Show call duration")

	show_call_duration_menu ="""
	1->Last call duration
	2->All calls duration
	3->Received calls duration
	4->Dialed calls duration
	5->Clear timers
	""";

	show_calls_duration_option = int(input(show_calls_duration_menu))
	if show_calls_duration_option == 1:
			print("last_call_duration")
	if show_calls_duration_option == 2:
			print("all_calls_duration")
	if show_calls_duration_option == 3:
			print("receieved_calls_duration")
	if show_calls_duration_option == 4:
			print("dailed_calls_duration")
	if show_calls_duration_option == 5:
			print("clear_timers")

	print("Show_call_costs")

	show_call_cost_menu ="""
	1->Last call cost
	2->All calls cost
	3->Clear counter
	""";

	show_calls_cost_option = int(input(show_calls_cost_menu))
	if show_calls_cost_option == 1:
			print("last_call_cost")
	if show_calls_cost_option == 2:
			print("all_calls_cost")
	if show_calls_cost_option == 3:
			print("clear_counters")

	print("Call_cost_settigs")

	7->call_cost_settings menu ="""
		1->Call cost limit
		2->Show costs in
		""";

	Call_cost_settings_option = int(input(call_cost_settings_menu))
		if call_cost_settings_option == 1:
			print("call_cost_limit")
		if call_cost_settings_option == 2:
			print("show_costs_in")

elif option == 5:
	print("Tones")

	tones_menu ="""
	1->Ringing tones
	2->Ringing volume
	3->Incoming call alert
	4->Composer
	5->Message alert tone
	6->Keypad tones
	7->Warning and game tones
	8->Viberating alert
	9->Screen saver
	""";

	Tones_option = int(input(tones_menu))
	if tones_option == 1:
		print("ringind_tones")
	if tones_option == 2:
		print("ringing_volume")
	if tones_option == 3:
		print("incoming_call_alert")
	if tones_option == 4:
		print("composer")
	if tones_option == 5:
		print("message_alert_tone")
	if tones_option == 6:
		print("keypad_tones")
	if tones_option == 7:
		print("warning_and_game_tones")
	if tones_option == 8:
		print("vibrating_alert")
	if tones_option == 9:
		print("screen_saver")

elif option == 6:
	print("Settings")

	1->Call_settings menu ="""
	  1->Automatic redial
	  2->Speed dialling
	  3->Call waiting option
	  4->Own sending option
	  5->Phone line in use
	  6->Automatic answer
	  """;

	call_settigs_option = int(input(call_settings_menu))
	if tones_option == 1:
		print("ringing_tones")
	if tones_option == 2:
		print("ringing_volume")
	if tones_option == 3:
		print("incoming_call_alert")
	if tones_option == 4:
		print("composer")
	if tones_option == 5:
		print("message_alert_tone")
	if tones_option == 6:
		print("keypad_tones")

	print("Phone_settings")

		phone_settings menu ="""
		1->Language
		2->Cell info display
		3->Welcome note
		4->Network selection
		5->Lights
		6->Confirm SIM service actions
		""";

	phone_settings_option = int(input(phone_settings_menu))
	if tones_option == 1:
		print("language")
	if tones_option == 2:
		print("cell_info_display")
	if tones_option == 3:
		print("welcome_note")
	if tones_option == 4:
		print("network_selection")
	if tones_option == 5:
		print("lights")
	if tones_option == 6:
		print("confirm_SIM_service_actions")
	
	3->Security settings
	  print("Security settings")

	  security_settings menu ="""
	  1->Pin code request
	  2->Call barring service
	  3->Fixed dialling
	  4->Closed user group
	  5->Phone security
	  6->Change access codes
	  """;

	security_settings_option = int(input(security_settings_menu))
	if tones_option == 1:
		print("pin_code_request")
	if tones_option == 2:
		print("call_barring_service")
	if tones_option == 3:
		print("fixed_dialing")
	if tones_option == 4:
		print("closed_user_group")
	if tones_option == 5:
		print("phone_security")
	if tones_option == 6:
		print("change_access_codes")

	4->Restore factory settings
	  print("Restore_factory_settings")

	  restore_factory_settings menu ="""
	  """;

       restore_factory_settings_option = int(input(security_settings_menu))
	if restore_factory_settings_option == 1:
		print("restore_factory_settings")


elif option == 7:
	print("Call divert")

	call_divert_menu ="""
	""";

	call_divert_option = int(input(call_divert_menu))
	if call_divert_option == 1:
		print("call_divert")


elif option == 8:
	print("Games")

	games_menu ="""
	""";

	games_option = int(input(games_menu))
	if games_option == 1:
		print("games")


elif option == 9:
	print("Calculator")

	calculator_menu ="""
	""";

	calculator_option = int(input(calculator_menu))
	if calculator_option == 1:
		print("calculator")

elif option == 10:
	print("Reminder")

	reminder_menu = """
	"""

	reminder_option = int(input(reminder_menu))
	if reminder_option == 1:
		print("reminder")

elif option == 11:
	print("Clock")


	clock_menu = """
	1->Alarm clock
	2->Clock settings
	3->Date settings
	4->Stopwatch
	5->Countdown timer
	6->Auto update of date and time
	"""

	clock_option = int(input(clock_menu))
	if clock_option == 1:
		print("alarm_clock")
	if clock_option == 2:
		print("clock_settings")
	if clock_option == 3:
		print("date_settings")
	if clock_option == 4:
		print("stopwatch")
	if clock_option == 5:
		print("countdown_timer")
	if clock_option == 6:
		print("auto_update_of_date_and_time")

elif option == 12:
	print("Profiles")

	profiles_menu ="""
	""";

	profiles_option = int(input(profles_menu))
	if profiles_option == 1:
		print("profiles")

elif option == 13:
	print("Sim_services")

	sim_services_menu ="""
	""";

	sim_services_option = int(input(sim_services_menu))
	if call_divert_option == 1:
		print("sim_services")