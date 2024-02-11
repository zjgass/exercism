defmodule RomanNumerals do
  @doc """
  Convert the number to a roman number.
  """
  def numeral(number) when number == 0 do
    ""
  end

  @spec numeral(pos_integer) :: String.t()
  def numeral(number) do
    {roman, next} = cond do
      number >= 1000 ->
        {"M", number - 1000}
      number >= 900 ->
        {"CM", number - 900}
      number >= 500 ->
        {"D", number - 500}
      number >= 400 ->
        {"CD", number - 400}
      number >= 100 ->
        {"C", number - 100}
      number >= 90 ->
        {"XC", number - 90}
      number >= 50 ->
        {"L", number - 50}
      number >= 40 ->
        {"XL", number - 40}
      number >= 10 ->
        {"X", number - 10}
      number >= 9 ->
        {"IX", number - 9}
      number >= 5 ->
        {"V", number - 5}
      number >= 4 ->
        {"IV", number - 4}
      number >= 1 ->
        {"I", number - 1}
    end

    roman <> numeral(next)
  end
end
