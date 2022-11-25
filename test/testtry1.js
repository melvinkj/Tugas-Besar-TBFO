let a = 13;

// trying nested try
try {
    try {
      throw "oops"
    } finally {
      throw "finally"
    }
  } catch (ex) {
    if (a < 5) {
        throw 1
    } else if (a < 10) {
        throw 2
    } else if (a < 15) {
        throw 3
    } else {
        throw 13
    }
  }