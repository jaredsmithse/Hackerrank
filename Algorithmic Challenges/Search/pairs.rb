def find_pairs(diff,ar)
	ar.sort!
	pairs = 0

	for i in ar
		for j in ar
			if i - j == diff
				pairs += 1

			end
		end
	end
	return pairs
end

puts find_pairs(2, [1,5,3,4,2])