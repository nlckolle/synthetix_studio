# Modulo del Motor de Ordenamiento desde Cero

class MotorOrdenamiento:
    """Implementacion manual de Mergesort para diagnosticos."""

    @staticmethod
    def mergesort(diagnosticos, criterio="line"):
        """Ordena recursivamente por 'line' o 'gravedad'."""
        if len(diagnosticos) <= 1:
            return diagnosticos

        medio = len(diagnosticos) // 2
        izq = MotorOrdenamiento.mergesort(diagnosticos[:medio], criterio)
        der = MotorOrdenamiento.mergesort(diagnosticos[medio:], criterio)

        return MotorOrdenamiento._merge(izq, der, criterio)

    @staticmethod
    def _merge(izq, der, criterio):
        resultado = []
        i = j = 0

        while i < len(izq) and j < len(der):
            if izq[i][criterio] <= der[j][criterio]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado