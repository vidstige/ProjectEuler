import Foundation  

struct Number: Codable, Comparable {
    static func < (lhs: Number, rhs: Number) -> Bool {
        // log both sides
        return Float(lhs.exponent) * log(Float(lhs.base)) < Float(rhs.exponent) * log(Float(rhs.base))
    }

    // Variables
    var base: Int
    var exponent: Int

    // Init
    init(_base: Int, _exponent: Int) {
        base = _base
        exponent = _exponent
    }
}

func gcd(_ m: Int, _ n: Int) -> Int {
    var a: Int = 0
    var b: Int = max(m, n)
    var r: Int = min(m, n)

    while r != 0 {
        a = b
        b = r
        r = a % b
    }
    return b
}

extension Array where Element: Comparable {
   var indexOfMax: Index? {
      guard var maxValue = self.first else { return nil }
      var maxIndex = 0

      for (index, value) in self.enumerated() {
         if value > maxValue {
            maxValue = value
            maxIndex = index
         }
     }

     return maxIndex
   }
}

func p99() -> Int {
    // Determine the file name
    let filename = "Data/base_exp.txt"

    // Read the contents of the specified file
    let contents = try! String(contentsOfFile: filename)

    // Split the file into separate lines
    let lines = contents.split(separator: "\n")
    let numbers = lines.map({ (line) -> Number in
        let parts = line.split(separator: ",")
        return Number(_base: Int(parts[0])!, _exponent: Int(parts[1])!)
    })

    return numbers.indexOfMax! + 1
}

// gcd(422489,979858)
print(p99())
