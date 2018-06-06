# Write a function to merge overlapping meetings 
def merge_meetings(meetings):
	# sort the list
	sorted_meetings = sorted(meetings)
	# store the first meeting in a variable
	merged_meetings = [sorted_meetings[0]]

	for meeting in sorted_meetings[1:]:
		current_meeting_start, current_meeting_end = meeting
		last_meeting_start, last_meeting_end = merged_meetings[-1]
		# if the current meeting starts after the previous meeting, merge
		if last_meeting_end >= current_meeting_start:
			merged_meetings[-1] = (last_meeting_start, max(last_meeting_end, current_meeting_end))
		# else, add this as a new meeting 
		else:
			merged_meetings.append(meeting)

	return merged_meetings 

# Test cases
# Remember: debugging is half the battle!
meetings = [(0,1), (3,5), (4,8), (10,12), (9,10)]
print merge_meetings(meetings)
