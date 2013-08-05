max_toys = 0
toy_prices = []
budget = 0

STDIN.each_with_index do |line, index|
	if index.zero?
		temp = line.split(" ")
		max_toys, budget = temp[0].to_i, temp[1].to_i
	elsif index == 1
		line.split(" ").each { |price| toy_prices << price.to_i }
	end

end

toy_prices.select! { |price| price < budget }

toys = []

toy_prices.sort.each do |toy_price|
	if toys.size.zero?
	  toys << toy_price
	  next
	end 
	toys << toy_price if (toys.size + 1 <= max_toys) && (toys.reduce(:+) + toy_price <= budget)
end

puts toys.size