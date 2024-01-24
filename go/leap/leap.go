// Package leap should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
// leap contains a function for determining if a given year is a leap
// year.
package leap

// IsLeapYear should have a comment documenting it.
// A year is a leeap year if it is evenly divisible by 4,
// but not if it is also evenly divisible by 100,
// unless it is also evenly divisible by 400.
func IsLeapYear(year int) bool {
	return (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
}
