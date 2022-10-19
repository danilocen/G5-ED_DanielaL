public class listasenlazadas{
    private node head;
    private node tail;
    private string name;

    public createList (string listname){
        name = listname;
        head = tail = null;
    }

    public bool isListEmpty(){
        if(head == null){
            return true
        }
        return false;
    }

    public void insertTailNode(int data){
        if(isListEmpty){
            head=tail=new node(data);
        }
        else{
            node n= new node(data);
            tail.next=n;
            tail=n;
        }
    }

    public void InsertNode(int data){
        if(isListEmpty){
            head=tail = new node(data);
        }
        else{
            node n= new node(data);
            tail.setNext=n;
            tail=n;
        }
    }

    public int deleteHead(){
        if(isListEmpty){
            throw new EmptyListException(name);
        }
        int deletedNode = head.getData;
        if(head==tail){
            head=tail=null;
        }
        else{
            head=head.next;
        }
    }
}



    


