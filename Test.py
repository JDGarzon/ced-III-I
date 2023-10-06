import unittest
import novel
class TestNovel(unittest.TestCase):

    def test_dialogos(self):
        self.assertEqual(novel.dialogos(0,"1"), 'Tu hija ha muerto. No hay nada más en tu cabeza en este momento. Ahogado en alcohol, no te importa ni tu trabajo, ni tu esposa, ni tu vida. Solo quieres una cosa, saber la respuesta. Te culpas por no haber estado más pendiente antes, por no haber indagado en su cambio drástico de actitud, ni en su completa falta de interés en ir al colegio, a pesar de que estaba a punto de graduarse. Todo por asumir que era algo típico de su adolescencia.  Su suicidio aún no está plenamente investigado, sin embargo, no tienes paciencia para esperar a la policía, quieres respuestas, y las buscarás por tu cuenta ( Necesitas información, divagando en dónde puedes encontrarla, a tu mente viene ir a la habitación de tu hija o ir a su colegio ¿qué decides hacer? )')
    
    def test_validate_name(self):
        self.assertTrue(novel.validate_name('Nombre'))
        self.assertFalse(novel.validate_name(''))

    def test_validate_answer(self):
        self.assertTrue(novel.validate_answer('a'))
        self.assertTrue(novel.validate_answer('b'))
        self.assertFalse(novel.validate_answer(''))
        self.assertFalse(novel.validate_answer('c'))
        self.assertFalse(novel.validate_answer('aa'))
        self.assertFalse(novel.validate_answer('ab'))
    
    def test_translate(self):
        stringToReplace="1"
        stringToTranslate=""
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), '1')
        stringToReplace="#$%"
        stringToTranslate="Nombre"
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), stringToTranslate)
        stringToReplace="Soy #$% y voy a mi casa"
        stringToTranslate="Alguien"
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), "Soy Alguien y voy a mi casa")

if __name__ == '__main__':
    unittest.main()