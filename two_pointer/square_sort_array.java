package dsa_with_dedication.two_pointer;

import java.util.* ;

public class square_sort_array
{
    public static int[] square_array(int arr[])
    {
        int n=arr.length;
        List<Integer>pos =new ArrayList<>();
        List<Integer>neg =new ArrayList<>();

        for(int i=0; i < n ; i++)
        {
            if( arr[i] >= 0 )
            {
                pos.add(arr[i]);
            }
            else
            {
                neg.add(arr[i]);
            }
        }
            if(neg.isEmpty())
            {
                for(int i = 0; i < pos.size(); i++)
                {   
                    pos.set(i, pos.get(i) * pos.get(i));
                }
                return pos.stream().mapToInt(Integer::intValue).toArray();
            }
            else if(pos.isEmpty())
            {
                for(int i = 0; i < neg.size(); i++)
                {
                    neg.set(i, neg.get(i) * neg.get(i));
                }
                Collections.reverse(neg);
                return neg.stream().mapToInt(Integer::intValue).toArray();
            }
            else
            {
                int k=0; 
                int p = pos.size();
                int q = neg.size();
                int res[]=new int[p+q];

                for(int i = 0; i < pos.size(); i++)
                {
                    pos.set(i, pos.get(i) * pos.get(i));
                }

                for(int i = 0; i < neg.size(); i++)
                {
                    neg.set(i, neg.get(i) * neg.get(i));
                }
                Collections.reverse(neg);


                int i=0 , j=0 ; // initialize two pointer i for pos and j for neg .

                while(i < pos.size() && j < neg.size())
                {
                    if(pos.get(i) <= neg.get(j))
                    {
                        res[k]=pos.get(i);
                        k++;
                        i++;
                    }
                    else
                    {
                        res[k]=neg.get(j);
                        k++;
                        j++;
                    }
                }
                while( i < pos.size())
                {
                    res[k]=pos.get(i);
                    k++;
                    i++;
                }
                while( j < neg.size())
                {
                    res[k]=neg.get(j);
                    k++;
                    j++;
                }
                return res;
            }
    }
    public static void main(String[] args) {
        int arr[]=new int[]{-7,-3,2,3,11};
        int res[]=square_array(arr);

        System.out.println("the resultant array is : ");
        
        for(int i : res)
        {
            System.out.println(i);
        }
    }
}