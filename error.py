class Error:
  def __init__(self, errtype, err):
    self.err = f"{errtype}:\n{err}"
  def __repr__(self):
    return self.err