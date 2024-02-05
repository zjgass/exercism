=begin
Write your code for the 'Raindrops' exercise in this file. Make the tests in
`raindrops_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/raindrops` directory.
=end

class Raindrops
  def self.convert(number)
    rain = ""
  
    if number % 3 == 0
      rain = "Pling"
    end
  
    if number % 5 == 0
      rain += "Plang"
    end
  
    if number % 7 == 0
      rain += "Plong"
    end
  
    if rain == ""
      rain += number.to_s
    end
  
    return rain
  end
end
