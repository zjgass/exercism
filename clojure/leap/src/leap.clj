(ns leap)

(defn leap-year? [year] ;; <- argslist goes here
  (if (= (mod year 400) 0) true (if (and (= (mod year 4) 0) (not= (mod year 100) 0)) true false))
)
