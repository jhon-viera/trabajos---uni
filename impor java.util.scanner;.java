impor java.util.scanner;
public class calculoimc
{
    static scanner entrada = new scanner(System.in);

    public static void main (String[]args)
    {
        float nombre,apellido,genero,edad,peso,estatura,imc;
        System.out.print("ingresar nombre");
        nombre=entrada.nextfloat();
        System.out.print("ingresar apellido");
        apellido=entrada.nextfloat()
        System.out.print("ingresar genero ");
        genero=entrada.nextfloat()
        System.out.print("ingresar edad ");
        edad=entrada.nextfloat()
        System.out.print("ingresar peso ");
        peso=entrada.nextfloat()
        System.out.print("ingresar estatura ");
        estatura=entrada.nextfloat()


        imc=peso / (altura**2);

        if(imc<18.5)
           System.out.print("bajo peso");
        else if(imc>18,5;imc<24;9);
               System.out:print("normal peso");
               else if(imc>25;imc<26,9)
                       System.out.print("sobrepeso gradoI");
                    else if (imc>27;imc<29.9)
                            System.out.print("sobre peso grado II");
                        else if (imc>30;imc<34.9)
                                System.out.print("obesidad tipo I");
                            else if(imc>35;imc<39.9)
                                  System.out.print("obesidad tipo II");
                                else if(imc>40;imc<49.9)
                                       System.out.print("obesidad de tipo III (morbidad) ");
                                    else if(imc>50)
                                           System.out.print("obesidad de tipo IV (extrema)")
                            

                        
    }


}