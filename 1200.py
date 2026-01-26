//FIXME to Python3
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> res = new ArrayList(); 
        Arrays.sort(arr);
        int min=Integer.MAX_VALUE;
        
        for(int i=0;i<arr.length-1;i++){
            int d = arr[i+1]-arr[i];
            if (d < min) {
                min=d;       
            }
        }
        
        for(int i=0;i<arr.length-1;i++){
            if(arr[i+1]-arr[i]==min){
                res.add(Arrays.asList(arr[i],arr[i+1]));
            }
        }
        return res;
    }
}
