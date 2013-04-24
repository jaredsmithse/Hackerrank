def compare(s1,s2)
	if s1.length > s2.length
		max = s2.length
	else
		max = s1.length
	end

	sim_count = 0

	i = 0
	while i < max 
		if s1[i] == s2[i]
			i += 1
			next
		else
			break
		end
	end

	return i

end

def find_similarity(s1)
	suffix = s1
	sim_sum = 0
	s1.length.times do |i|
		sim_sum += compare(s1,suffix)
		suffix = suffix[1..-1]
	end

	return sim_sum

end

runs = ARGV[0]
puts runs
runs.times do |i|
	next if i == 0
	puts find_similarity(ARGV[i])
end