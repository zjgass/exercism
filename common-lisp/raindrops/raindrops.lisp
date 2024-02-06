(defpackage :raindrops
  (:use :cl)
  (:export :convert))

(in-package :raindrops)

(defun convert (n)
  "Converts a number to a string of raindrop sounds."
  (let ((rain ""))
    (if (eql (mod n 3) 0) (setq rain (concatenate 'string rain "Pling")))
    (if (eql (mod n 5) 0) (setq rain (concatenate 'string rain "Plang")))
    (if (eql (mod n 7) 0) (setq rain (concatenate 'string rain "Plong")))
    (if (string= rain "") (write-to-string n) rain))
)
