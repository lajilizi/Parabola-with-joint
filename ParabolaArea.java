import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class ParabolaArea extends JFrame{
    public void MainFrame () {
    	this.setTitle("计算抛物线围成面积");
    	this.setSize(300,150);
    	this.setVisible(true);
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
    new ParabolaArea();
    while(0<1) {
        System.out.println("y=ax^2+bx+c");
        Scanner sc = new Scanner(System.in);
        System.out.println("a=");
        float a = sc.nextFloat();
        if(a == 0) {
        	System.out.println("无效数据");
        	continue;
        }
        
    	System.out.println("输入交点");
    	System.out.println("x1=");
    	float x1 = sc.nextFloat();
    	System.out.println("x2=");
    	float x2 = sc.nextFloat();
    	float h = (a * (x1*x1 +x2*x2 -2*x1*x2)/2);
    	float g = (x1 - x2);
    	if(h<0) {
    		h = (-1) * h;
	}
    	if(g<0) {
    		g = (-1) *g;
    	}
        float S1 = h * g / 3;
        System.out.println(S1);
}
	}
}
