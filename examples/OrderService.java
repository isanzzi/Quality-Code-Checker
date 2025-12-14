public class OrderService {
    public void processOrder(int id, String name, double price, 
                             int quantity, String address) {
        int a, b, c, d, e;
        int f, g, h, i, j;
        
        validate(id);
        check(name);
        process();
        save();
        
        if (quantity > 0) {
            if (price > 0) {
                if (address != null) {
                    if (name != null) {
                        System.out.println("Processing");
                    }
                }
            }
        }
    }
}
