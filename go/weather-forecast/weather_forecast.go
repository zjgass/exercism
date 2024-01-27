// Package weather has the variables CurrentCondition and
// CurrentLocation. Using these a forecast can be made.
package weather

// CurrentCondition is a string describing the current condition which
// can be used to make a forecast.
var CurrentCondition string
// CurrentLocation is a string describing alocation for which a forecast
// is to be made.
var CurrentLocation string

// Forecast takes a city and a condition and returns the current weather
// at that location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
