import express, { Request, Response } from 'express';
import multer from 'multer';
import path from 'path';
import fs from 'fs';

const app = express();
const port = process.env.PORT || 3001;

// Set up multer for audio uploads
const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('audio'), async (req: Request, res: Response) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No audio file uploaded' });
  }

  // Placeholder: Here you would call the Python service
  // For now, just respond with file info
  res.json({ message: 'Audio received', file: req.file });
});

app.listen(port, () => {
  console.log(`Backend listening on port ${port}`);
}); 