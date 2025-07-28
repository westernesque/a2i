"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const multer_1 = __importDefault(require("multer"));
const axios_1 = __importDefault(require("axios"));
const form_data_1 = __importDefault(require("form-data"));
const path_1 = __importDefault(require("path"));
const fs_1 = __importDefault(require("fs"));
const app = (0, express_1.default)();
const port = 3000;
// Configure multer for file uploads
const upload = (0, multer_1.default)({
    dest: 'uploads/',
    limits: {
        fileSize: 50 * 1024 * 1024 // 50MB limit
    }
});
// Configure Python service URL
const PYTHON_SERVICE_URL = 'http://localhost:5001';
// Middleware
app.use(express_1.default.json());
app.use(express_1.default.static(path_1.default.join(__dirname, '../../frontend')));
// CORS middleware
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});
// Health check endpoint
app.get('/health', (req, res) => {
    res.json({
        status: 'ok',
        service: 'audio-to-image-backend',
        timestamp: Date.now()
    });
});
// Upload endpoint
app.post('/upload', upload.single('audio'), async (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'No audio file provided' });
    }
    try {
        console.log(`📁 Processing file: ${req.file.originalname}`);
        // Create form data for Python service
        const formData = new form_data_1.default();
        formData.append('audio', fs_1.default.createReadStream(req.file.path));
        // Call Python service
        console.log('🔄 Calling Python service...');
        const response = await axios_1.default.post(`${PYTHON_SERVICE_URL}/upload`, formData, {
            headers: {
                ...formData.getHeaders(),
            },
            timeout: 300000, // 5 minutes timeout
        });
        const result = response.data;
        if (result.success) {
            console.log('✅ Two-stage pipeline completed successfully');
            // Return the results
            res.json({
                success: true,
                message: 'Two-stage pipeline completed successfully',
                abstract_image: result.abstract_image,
                representational_image: result.representational_image,
                features: result.features,
                transcription: result.transcription,
                abstract_prompt: result.abstract_prompt,
                representational_prompt: result.representational_prompt
            });
        }
        else {
            console.error('❌ Python service error:', result.error);
            res.status(500).json({
                success: false,
                error: result.error || 'Unknown error from Python service'
            });
        }
    }
    catch (error) {
        console.error('❌ Upload error:', error);
        if (axios_1.default.isAxiosError(error)) {
            if (error.code === 'ECONNREFUSED') {
                res.status(503).json({
                    success: false,
                    error: 'Python service is not running. Please start the Python service first.'
                });
            }
            else if (error.response) {
                res.status(error.response.status).json({
                    success: false,
                    error: error.response.data?.error || 'Python service error'
                });
            }
            else {
                res.status(500).json({
                    success: false,
                    error: 'Network error when calling Python service'
                });
            }
        }
        else {
            res.status(500).json({
                success: false,
                error: 'Internal server error'
            });
        }
    }
    finally {
        // Clean up uploaded file
        if (req.file && fs_1.default.existsSync(req.file.path)) {
            fs_1.default.unlinkSync(req.file.path);
        }
    }
});
// Serve images from Python service
app.get('/images/:filename', async (req, res) => {
    try {
        const filename = req.params.filename;
        const imageUrl = `${PYTHON_SERVICE_URL}/images/${filename}`;
        const response = await axios_1.default.get(imageUrl, {
            responseType: 'stream'
        });
        res.setHeader('Content-Type', 'image/png');
        response.data.pipe(res);
    }
    catch (error) {
        console.error('❌ Image serving error:', error);
        res.status(404).json({ error: 'Image not found' });
    }
});
// Root route - serve the frontend
app.get('/', (req, res) => {
    res.sendFile(path_1.default.join(__dirname, '../../frontend/index.html'));
});
// Start server
app.listen(port, () => {
    console.log(`🚀 Backend server running on http://localhost:${port}`);
    console.log(`📁 Serving frontend from: ${path_1.default.join(__dirname, '../../frontend')}`);
    console.log(`🔗 Python service URL: ${PYTHON_SERVICE_URL}`);
});
