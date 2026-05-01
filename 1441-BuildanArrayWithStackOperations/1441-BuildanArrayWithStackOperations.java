// Last updated: 01/05/2026, 08:21:57
class Solution {
    public List<String> buildArray(int[] target, int n) {
        int last=target[target.length-1];
int j=0;
        List<String> answer=new ArrayList<>();
List<Integer> list = Arrays.stream(target)
                           .boxed() 
                           .toList(); 
      for(int i=1;i<=last;i++){
        answer.add("Push");
        if(target[j]==i){
            j++;
        }
        else{
    answer.add("Pop");
    }
}

//         if(list.contains(i)!=true){
// answer.add("Pop");
//         }

                           


        return answer;
    }
}