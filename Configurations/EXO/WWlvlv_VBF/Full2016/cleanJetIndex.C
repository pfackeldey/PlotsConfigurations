int cleanJetIndex(int match0, int match1, int resultingIndex){
  if ((match0 == 1) && (match1 == 1)){
    if (resultingIndex == 0)
      return 2;
    else 
      return 3;
  } else if ((match0 == 1) && (match1 == 0)){
    if (resultingIndex == 0)
      return 1;
    else 
      return 2;
  } else if ((match0 == 0) && (match1 == 1)){
    if (resultingIndex == 0)
      return 0;
    else
      return 2;
  } else {
    if (resultingIndex == 0)
      return 0;
    else
      return 1;
  }
}
