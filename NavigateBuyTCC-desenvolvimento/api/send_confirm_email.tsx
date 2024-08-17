// pages/api/send_confirmation_email.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import nodemailer from 'nodemailer';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { email } = req.body;

    // Configurar o transporte de e-mail
    const transporter = nodemailer.createTransport({
      service: 'Gmail',
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS,
      },
    });

    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: email,
      subject: 'Código de Confirmação',
      text: 'Seu código de confirmação é: 123456', // Substitua pelo código gerado
    };

    try {
      await transporter.sendMail(mailOptions);
      res.status(200).json({ message: 'Código de confirmação enviado para o e-mail.' });
    } catch (error) {
      res.status(500).json({ message: 'Erro ao enviar o e-mail.' });
    }
  } else {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
