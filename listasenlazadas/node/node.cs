public class node{
    private int data;
    private node next;

    public void createNode(int data){
        this.data = data;
        this.next = null;
    }
    public int getData(){
        return data;
    }
    public void setData(int data){
        this.data = data;
    }
    public node getNext(){
        return next;
    }
    public void setNext(int data, node next){
        this.data = data;
        this.next = next;
    }
}