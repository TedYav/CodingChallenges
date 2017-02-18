/*

   Sentence Reverse:
   
   Strategy:
      Suboptimal:
         Create new array []
         Iterate through arr
         For each word...
      Better:
         Reverse whole array and reverse one by one

 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' 
 
 ==>
 'e','c','i','t','c','a','r','p' wordStart = 0, i=8
 0 , 1,   2,  3,  4,  5,  6,  7
*/



function sentenceReverse(sentence){
   sentence = sentence.reverse();
   wordStart = 0;
   for(let i = 0; i<sentence.length; i++){
      if(i==' '){
         for(j=wordStart;j< (i - wordStart)/2 + wordStart ;j++){
            let tmp = sentence[j];
            sentence[j] = sentence[i - (j-wordStart) - 1];
            sentence[i - (j-wordStart) - 1] = tmp;
         }
         wordStart = i+1;
      }
   }
   return sentence;
}