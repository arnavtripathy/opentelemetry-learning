#docker command - docker run -d -p 4317:4317 -p 16686:16686 --name jaeger jaegertracing/all-in-one:latest

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
import time

# Configure OTLP Exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")

# Set up the Tracer Provider with a service name
provider = TracerProvider(
    resource=Resource.create({"service.name": "jaeger-service"})
)
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)

# Set the global tracer provider
trace.set_tracer_provider(provider)

# Create a tracer
tracer = trace.get_tracer("my.tracer.name")

@tracer.start_as_current_span("add")
def add(first, second):
    third = multiply(first, second)
    third = 0
    return first + second + third

@tracer.start_as_current_span("multiply")
def multiply(first, second):
    return first * second

print(add(2, 3))


# Give time for spans to be exported
time.sleep(5)