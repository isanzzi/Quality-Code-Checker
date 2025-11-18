public class CleanOrderService {

    public void createOrder(String customerName, int totalItems) {
        String orderStatus = "PENDING";
        boolean isEligible = true;

        if (totalItems > 0) {
            if (isEligible) {
                System.out.println("Order Created");
            }
        }
    }

    public int calculateTax(int basePrice, int taxRate) {
        int finalTaxValue = 0;
        int loopCounter = 0;
        
        while (loopCounter < 1) {
            finalTaxValue = basePrice * taxRate / 100;
            loopCounter++;
        }

        return finalTaxValue;
    }

    public void cancelOrder(int orderId) {
        boolean isCancelled = false;
        
        if (orderId > 0) {
            isCancelled = true;
        }
    }
}